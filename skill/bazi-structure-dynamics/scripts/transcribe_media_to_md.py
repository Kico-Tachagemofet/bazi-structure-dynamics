from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def safe_stem(path: Path) -> str:
    stem = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "_", path.stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem[:160] or "transcript"


def fmt_time(seconds: float) -> str:
    total_ms = max(0, int(round(float(seconds) * 1000)))
    ms = total_ms % 1000
    total_s = total_ms // 1000
    second = total_s % 60
    total_m = total_s // 60
    minute = total_m % 60
    hour = total_m // 60
    return f"{hour:02d}:{minute:02d}:{second:02d}.{ms:03d}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe a local audio/video file into timestamped Markdown."
    )
    parser.add_argument("media", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--packages", type=Path, required=True)
    parser.add_argument("--language", default="zh")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--initial-prompt")
    args = parser.parse_args()

    if not args.media.is_file():
        raise FileNotFoundError(args.media)
    if not args.packages.is_dir():
        raise FileNotFoundError(args.packages)

    sys.path.insert(0, str(args.packages.resolve()))
    from faster_whisper import WhisperModel

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = safe_stem(args.media)
    md_path = args.out_dir / f"{stem}.md"
    txt_path = args.out_dir / f"{stem}.txt"

    model = WhisperModel(
        args.model,
        device="cpu",
        compute_type="int8",
        local_files_only=True,
    )
    segments_iter, info = model.transcribe(
        str(args.media),
        language=args.language,
        task="transcribe",
        beam_size=args.beam_size,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
        condition_on_previous_text=True,
        initial_prompt=args.initial_prompt,
    )

    segments: list[tuple[float, float, str]] = []
    for segment in segments_iter:
        segment_text = segment.text.strip()
        if not segment_text:
            continue
        segments.append((segment.start, segment.end, segment_text))
        print(
            f"[{fmt_time(segment.start)} -> {fmt_time(segment.end)}] {segment_text}",
            flush=True,
        )

    plain_text = "\n".join(text for _, _, text in segments)
    header = [
        f"# {args.media.name}",
        "",
        f"- 来源文件：`{args.media.resolve()}`",
        f"- 识别语言：{info.language}",
        f"- 语言置信度：{info.language_probability:.3f}",
        f"- 媒体时长：{fmt_time(info.duration)}",
        f"- 模型：faster-whisper `{args.model}`",
        "- 状态：自动转录，干支、术语、命例及关键断语尚待对照音视频复核",
        "",
        "## 纯文本",
        "",
        plain_text,
        "",
        "## 时间戳逐段转录",
        "",
    ]
    timestamp_lines = [
        f"- [{fmt_time(start)} -> {fmt_time(end)}] {segment_text}"
        for start, end, segment_text in segments
    ]
    md_path.write_text("\n".join(header + timestamp_lines) + "\n", encoding="utf-8")
    txt_path.write_text(plain_text + "\n", encoding="utf-8")

    print(f"Wrote Markdown: {md_path.resolve()}")
    print(f"Wrote text: {txt_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

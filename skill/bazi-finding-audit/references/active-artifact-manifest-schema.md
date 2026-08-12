# Active Artifact Manifest Schema

`active-artifact-manifest.json` 解决“旧文件仍留在案例目录，runtime 不知道该读哪份”的问题。它不删除历史产物，只把每个可路由下游文件明确标为 active 或 inactive。

## Header

- `schema_version: "1.0"`
- `case_id`
- `current_structure_freeze_id`
- `active_artifacts`
- `inactive_artifacts`

## Active Artifact

- `path`：案例目录相对路径
- `stage`
- `structure_freeze_id`
- `dependencies`：案例目录相对路径

文件自身必须声明同一个 `structure_freeze_id`。其依赖必须存在；若依赖也是下游 active artifact，二者须指向同一 freeze。

## Inactive Artifact

- `path`
- `reason`：如 `superseded`／`retracted`／`failed-audit`／`historical`
- `superseded_by`：可为 `null`

Topic lens、index、imagery packet、coverage、pillar composite、axis scene、topic finding、composition 与 final reading 等可路由文件必须全部出现在 active 或 inactive 清单。未归类即 FAIL；不靠文件名中的 `old`、`v2` 或一段撤回说明猜测状态。

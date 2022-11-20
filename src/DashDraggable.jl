
module DashDraggable
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.1.1a"

include("dashboarditem.jl")
include("dashboarditemresponsive.jl")
include("draggabledashboard.jl")
include("draggabledashboardresponsive.jl")
include("gridlayout.jl")
include("responsivegridlayout.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_draggable",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_draggable.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_draggable.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end

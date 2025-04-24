# V1VirtualMachineInstanceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vsockcid** | **int** | VSOCKCID is used to track the allocated VSOCK CID in the VM. | [optional] 
**active_pods** | **dict(str, str)** | ActivePods is a mapping of pod UID to node name. It is possible for multiple pods to be running for a single VMI during migration. | [optional] 
**conditions** | [**list[V1VirtualMachineInstanceCondition]**](V1VirtualMachineInstanceCondition.md) | Conditions are specific points in VirtualMachineInstance&#39;s pod runtime. | [optional] 
**current_cpu_topology** | [**V1CPUTopology**](V1CPUTopology.md) | CurrentCPUTopology specifies the current CPU topology used by the VM workload. Current topology may differ from the desired topology in the spec while CPU hotplug takes place. | [optional] 
**evacuation_node_name** | **str** | EvacuationNodeName is used to track the eviction process of a VMI. It stores the name of the node that we want to evacuate. It is meant to be used by KubeVirt core components only and can&#39;t be set or modified by users. | [optional] 
**fs_freeze_status** | **str** | FSFreezeStatus indicates whether a freeze operation was requested for the guest filesystem. It will be set to \&quot;frozen\&quot; if the request was made, or unset otherwise. This does not reflect the actual state of the guest filesystem. | [optional] 
**guest_os_info** | [**V1VirtualMachineInstanceGuestOSInfo**](V1VirtualMachineInstanceGuestOSInfo.md) | Guest OS Information | [optional] 
**interfaces** | [**list[V1VirtualMachineInstanceNetworkInterface]**](V1VirtualMachineInstanceNetworkInterface.md) | Interfaces represent the details of available network interfaces. | [optional] 
**kernel_boot_status** | [**V1KernelBootStatus**](V1KernelBootStatus.md) | KernelBootStatus contains info about the kernelBootContainer | [optional] 
**launcher_container_image_version** | **str** | LauncherContainerImageVersion indicates what container image is currently active for the vmi. | [optional] 
**machine** | [**V1Machine**](V1Machine.md) | Machine shows the final resulting qemu machine type. This can be different than the machine type selected in the spec, due to qemus machine type alias mechanism. | [optional] 
**memory** | [**V1MemoryStatus**](V1MemoryStatus.md) | Memory shows various informations about the VirtualMachine memory. | [optional] 
**migrated_volumes** | [**list[V1StorageMigratedVolumeInfo]**](V1StorageMigratedVolumeInfo.md) | MigratedVolumes lists the source and destination volumes during the volume migration | [optional] 
**migration_method** | **str** | Represents the method using which the vmi can be migrated: live migration or block migration | [optional] 
**migration_state** | [**V1VirtualMachineInstanceMigrationState**](V1VirtualMachineInstanceMigrationState.md) | Represents the status of a live migration | [optional] 
**migration_transport** | **str** | This represents the migration transport | [optional] 
**node_name** | **str** | NodeName is the name where the VirtualMachineInstance is currently running. | [optional] 
**phase** | **str** | Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it. | [optional] 
**phase_transition_timestamps** | [**list[V1VirtualMachineInstancePhaseTransitionTimestamp]**](V1VirtualMachineInstancePhaseTransitionTimestamp.md) | PhaseTransitionTimestamp is the timestamp of when the last phase change occurred | [optional] 
**qos_class** | **str** | The Quality of Service (QOS) classification assigned to the virtual machine instance based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md  Possible enum values:  - &#x60;\&quot;BestEffort\&quot;&#x60; is the BestEffort qos class.  - &#x60;\&quot;Burstable\&quot;&#x60; is the Burstable qos class.  - &#x60;\&quot;Guaranteed\&quot;&#x60; is the Guaranteed qos class. | [optional] 
**reason** | **str** | A brief CamelCase message indicating details about why the VMI is in this state. e.g. &#39;NodeUnresponsive&#39; | [optional] 
**runtime_user** | **int** | RuntimeUser is used to determine what user will be used in launcher | [optional] [default to 0]
**selinux_context** | **str** | SELinuxContext is the actual SELinux context of the virt-launcher pod | [optional] 
**topology_hints** | [**V1TopologyHints**](V1TopologyHints.md) |  | [optional] 
**virtual_machine_revision_name** | **str** | VirtualMachineRevisionName is used to get the vm revision of the vmi when doing an online vm snapshot | [optional] 
**volume_status** | [**list[V1VolumeStatus]**](V1VolumeStatus.md) | VolumeStatus contains the statuses of all the volumes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



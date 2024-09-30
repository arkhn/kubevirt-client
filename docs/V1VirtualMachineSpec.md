# V1VirtualMachineSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_volume_templates** | [**list[V1DataVolumeTemplateSpec]**](V1DataVolumeTemplateSpec.md) | dataVolumeTemplates is a list of dataVolumes that the VirtualMachineInstance template can reference. DataVolumes in this list are dynamically created for the VirtualMachine and are tied to the VirtualMachine&#39;s life-cycle. | [optional] 
**instancetype** | [**V1InstancetypeMatcher**](V1InstancetypeMatcher.md) | InstancetypeMatcher references a instancetype that is used to fill fields in Template | [optional] 
**preference** | [**V1PreferenceMatcher**](V1PreferenceMatcher.md) | PreferenceMatcher references a set of preference that is used to fill fields in Template | [optional] 
**run_strategy** | **str** | Running state indicates the requested running state of the VirtualMachineInstance mutually exclusive with Running | [optional] 
**running** | **bool** | Running controls whether the associatied VirtualMachineInstance is created or not Mutually exclusive with RunStrategy Deprecated: VirtualMachineInstance field \&quot;Running\&quot; is now deprecated, please use RunStrategy instead. | [optional] 
**template** | [**V1VirtualMachineInstanceTemplateSpec**](V1VirtualMachineInstanceTemplateSpec.md) | Template is the direct specification of VirtualMachineInstance | 
**update_volumes_strategy** | **str** | UpdateVolumesStrategy is the strategy to apply on volumes updates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



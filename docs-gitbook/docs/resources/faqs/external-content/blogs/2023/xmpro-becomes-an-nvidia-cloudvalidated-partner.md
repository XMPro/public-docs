# XMPro becomes an NVIDIA Cloud-Validated partner

[**Blog**](https://xmpro.com/category/blog/)

## XMPro becomes an NVIDIA Cloud-Validated partner

Posted on [November 2, 2023](https://xmpro.com/xmpro-becomes-an-nvidia-cloud-validated-partner/) by [Sarah Danks](https://xmpro.com/author/sarah/)![](https://xmpro.com/wp-content/uploads/2023/09/MicrosoftTeams-image-48.png)

**By Daniel King, XMPro Development Manager**

This week XMPro announced that it has become an [NVIDIA Cloud-Validated partner.](https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro) By using the NVIDIA AI platform, we are better positioned to support customers to bridge the gap between data flow and operational AI in the cloud.

To get here, we completed a rigorous test plan to validate and showcase the XMPro Suite running efficiently on NVIDIA’s technology stack. This included building an agent to process a sample AI workload using NVIDIA GPUs (via CUDA) to showcase how the XMPro suite runs optimally on the NVIDIA stack.

And how did we do this, you ask? The following steps outline the process we used to test XMPro on an NVIDIA GPU.

![](https://xmpro.com/wp-content/uploads/2023/09/NVIDIA-Blog-1.png)

Step One: Build an Agent – Follow our docs to [build](https://documentation.xmpro.com/how-tos/agents/building-agents) and [package](https://documentation.xmpro.com/how-tos/agents/packaging-agents) an Agent. Import your preferred CUDA NuGet package when building your agent. In this example we used [ILGPU](https://nugetmusthaves.com/Package/ILGPU).

You can find a [list of popular libraries in NuGet](https://nugetmusthaves.com/tag/cuda).

Step Two: Provision an NVIDIA GPU service in the cloud – Provision your preferred [NVIDIA Virtual Machine Image and cloud provider](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nvidia_vmi).

Step Three: Install Stream Host – Follow the [docs to install the XMPro Stream Host](https://documentation.xmpro.com/installation/3.-complete-installation/install-stream-host/ubuntu-16.04+-x64) on Ubuntu 20.04 using the provisioned virtual machine in step two.

Step Four: Add the Agent to a Stream – [Import an agent](https://documentation.xmpro.com/concepts/agent), [add to a stream](https://documentation.xmpro.com/how-tos/data-streams), configure the agent and [publish the stream](https://documentation.xmpro.com/how-tos/publish).

_This is an example of an Agent that calculates the number of prime numbers in a given number using concurrent processing on an NVIDIA GPU running in AWS. It is implemented in a stream that increases the number every second by 500,000._![](https://xmpro.com/wp-content/uploads/2023/09/Nvidia-Take-2.gif)

The primary objective of NVIDIA cloud validation is to help customers easily identify and adopt validated NVIDIA-based solutions. XMPro is now part of the [NVIDIA ](https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro)[Accelerated Applications ](https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro)[Catalog](https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro), which features world-class GPU- and DPU-accelerated solutions.

**About Daniel King:** Daniel King is Development Manager for XMPro, with 19 years of experience in development and solution architecture. He designs simple solutions to complex problems that deliver business value.



<article class="post-14202 post type-post status-publish format-standard has-post-thumbnail hentry category-blog tag-ai tag-nvidia tag-product-update" id="post-14202">
<div class="article-inner">
<header class="entry-header">
<div class="entry-header-text entry-header-text-top text-center">
<h6 class="entry-category is-xsmall"><a href="https://xmpro.com/category/blog/" rel="category tag">Blog</a></h6><h1 class="entry-title">XMPro Suite on NVIDIA Cloud GPUs</h1><div class="entry-divider is-divider small"></div>
<div class="entry-meta uppercase is-xsmall">
<span class="posted-on">Posted on <a href="https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/" rel="bookmark"></a></span> <span class="byline">by <span class="meta-author vcard"><a class="url fn n" href="https://xmpro.com/author/sarah/">Sarah Danks</a></span></span> </div>
</div>
</header>
<div class="entry-content single-page">
<div class="row" id="row-1819164801">
<div class="col small-12 large-12" id="col-1702010517">
<div class="col-inner">
<div class="img has-hover x md-x lg-x y md-y lg-y" id="image_1155825663">
<div class="img-inner dark">
<img height="667" src="https://xmpro.com/wp-content/uploads/2023/09/MicrosoftTeams-image-48.png" width="1000"/>

</div>
<style>
#image_1155825663 {
  width: 100%;
}
</style>
</div>
<h4><span class="TextRun SCXW177798882 BCX9" data-contrast="auto" lang="EN-AU" xml:lang="EN-AU"><span class="NormalTextRun SCXW177798882 BCX9">By Daniel King, XMPro Development Manager</span></span></h4>
<div class="is-divider divider clearfix"></div>
<p style="font-weight: 400;">This week XMPro announced that it has become an <a href="https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro">NVIDIA Cloud-Validated partner.</a> By using the NVIDIA AI platform, we are better positioned to support customers to bridge the gap between data flow and operational AI in the cloud.</p>
<p style="font-weight: 400;">To get here, we completed a rigorous test plan to validate and showcase the XMPro Suite running efficiently on NVIDIA’s technology stack. This included building an agent to process a sample AI workload using NVIDIA GPUs (via CUDA) to showcase how the XMPro suite runs optimally on the NVIDIA stack.</p>
<p style="font-weight: 400;">And how did we do this, you ask? The following steps outline the process we used to test XMPro on an NVIDIA GPU.</p>
<p><a href="#_ednref1" name="_edn1"></a></p>
<div class="gap-element clearfix" id="gap-57632721" style="display:block; height:auto;">
<style>
#gap-57632721 {
  padding-top: 30px;
}
</style>
</div>
</div>
</div>
</div>
<div class="img has-hover x md-x lg-x y md-y lg-y" id="image_1272418460">
<div class="img-inner dark">
<img height="496" src="https://xmpro.com/wp-content/uploads/2023/09/NVIDIA-Blog-1.png" width="606"/>

</div>
<style>
#image_1272418460 {
  width: 100%;
}
</style>
</div>
<div class="gap-element clearfix" id="gap-1589249318" style="display:block; height:auto;">
<style>
#gap-1589249318 {
  padding-top: 30px;
}
</style>
</div>
<div>
<p class="paragraph"><span class="normaltextrun"><b><span lang="EN-US">Step One: Build an Agent – </span></b></span><span class="normaltextrun"><span lang="EN-US">Follow our </span></span>docs to <a href="https://documentation.xmpro.com/how-tos/agents/building-agents"><span lang="EN-US">build</span></a><span lang="EN-US"> and </span><a href="https://documentation.xmpro.com/how-tos/agents/packaging-agents"><span lang="EN-US">package</span></a> an Agent. Import your preferred CUDA NuGet package when building your agent. In this example we used <a href="https://nugetmusthaves.com/Package/ILGPU">ILGPU</a>.</p>
</div>
<div>
<p class="paragraph">You can find a <a href="https://nugetmusthaves.com/tag/cuda">list of popular libraries in NuGet</a>.</p>
</div>
<div>
<p class="paragraph"><span class="normaltextrun"><b><span lang="EN-US">Step Two: Provision an NVIDIA GPU service in the cloud – </span></b></span><span class="normaltextrun"><span lang="EN-US">Provision your preferred </span></span><a href="https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nvidia_vmi"><span lang="EN-US">NVIDIA Virtual Machine Image and cloud provider</span></a><span class="normaltextrun"><span lang="EN-US">.</span></span></p>
<div>
<p class="paragraph"><span class="normaltextrun"><b><span lang="EN-US">Step Three: Install Stream Host – </span></b></span><span class="normaltextrun"><span lang="EN-US">Follow the </span></span><a href="https://documentation.xmpro.com/installation/3.-complete-installation/install-stream-host/ubuntu-16.04+-x64"><span lang="EN-US">docs to install the XMPro Stream Host</span></a><span class="normaltextrun"><span lang="EN-US"> on Ubuntu 20.04 using the provisioned virtual machine in step two.</span></span></p>
</div>
<div>
<p class="paragraph"><span class="normaltextrun"><b><span lang="EN-US">Step Four: Add the Agent to a Stream – </span></b></span><a href="https://documentation.xmpro.com/concepts/agent"><span lang="EN-US">Import an agent</span></a><span class="normaltextrun"><span lang="EN-US">, </span></span><a href="https://documentation.xmpro.com/how-tos/data-streams"><span lang="EN-US">add to a stream</span></a><span class="normaltextrun"><span lang="EN-US">, configure the agent and </span></span><a href="https://documentation.xmpro.com/how-tos/publish"><span lang="EN-US">publish the stream</span></a><span class="normaltextrun"><span lang="EN-US">. </span></span></p>
</div>
<div><span class="normaltextrun"><i><span lang="EN-US">This is an example of an Agent that calculates the number</span></i><i><span lang="EN-US"> of prime numbers in a given number using concurrent processing on an NVIDIA GPU running in AWS. It is implemented in a stream that increases the number every second by 500,000.</span></i></span></div>
</div>
<div> </div>
<div class="img has-hover x md-x lg-x y md-y lg-y" id="image_1265832624">
<div class="img-inner dark">
<img height="1080" src="https://xmpro.com/wp-content/uploads/2023/09/Nvidia-Take-2.gif" width="1920"/>

</div>
<style>
#image_1265832624 {
  width: 100%;
}
</style>
</div>
<div class="gap-element clearfix" id="gap-139402554" style="display:block; height:auto;">
<style>
#gap-139402554 {
  padding-top: 30px;
}
</style>
</div>
<p style="font-weight: 400;">The primary objective of NVIDIA cloud validation is to help customers easily identify and adopt validated NVIDIA-based solutions. XMPro is now part of the <a href="https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro">NVIDIA </a><a href="https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro">Accelerated Applications </a><a href="https://www.nvidia.com/en-us/gpu-accelerated-applications/?search=xmpro">Catalog</a>, which features world-class GPU- and DPU-accelerated solutions.</p>
<p style="font-weight: 400;"><strong>About Daniel King:</strong> Daniel King is Development Manager for XMPro, with 19 years of experience in development and solution architecture. He designs simple solutions to complex problems that deliver business value.</p>
<div class="gap-element clearfix" id="gap-1875695520" style="display:block; height:auto;">
<style>
#gap-1875695520 {
  padding-top: 30px;
}
</style>
</div>
<div class="blog-share text-center"><div class="is-divider medium"></div><div class="social-icons share-icons share-row relative"><a aria-label="Share on WhatsApp" class="icon button circle is-outline tooltip whatsapp show-for-medium" data-action="share/whatsapp/share" href="whatsapp://send?text=XMPro%20Suite%20on%20NVIDIA%20Cloud%20GPUs - https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/" title="Share on WhatsApp"><i class="icon-whatsapp"></i></a><a aria-label="Share on Facebook" class="icon button circle is-outline tooltip facebook" data-label="Facebook" href="https://www.facebook.com/sharer.php?u=https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/" onclick="window.open(this.href,this.title,'width=500,height=500,top=300px,left=300px'); return false;" rel="noopener nofollow" target="_blank" title="Share on Facebook"><i class="icon-facebook"></i></a><a aria-label="Share on Twitter" class="icon button circle is-outline tooltip twitter" href="https://twitter.com/share?url=https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/" onclick="window.open(this.href,this.title,'width=500,height=500,top=300px,left=300px'); return false;" rel="noopener nofollow" target="_blank" title="Share on Twitter"><i class="icon-twitter"></i></a><a aria-label="Email to a Friend" class="icon button circle is-outline tooltip email" href="/cdn-cgi/l/email-protection#18276b6d7a727d7b6c254055486a773d2a284b6d716c7d3d2a2877763d2a28564e515c51593d2a285b74776d7c3d2a285f484d6b3e7a777c61255b707d7b733d2a286c70716b3d2a28776d6c3d2b593d2a28706c6c686b3d2b593d2a5e3d2a5e6075686a77367b77753d2a5e6075686a77356b6d716c7d35777635766e717c7179357b74776d7c357f686d6b3d2a5e" rel="nofollow" title="Email to a Friend"><i class="icon-envelop"></i></a><a aria-label="Pin on Pinterest" class="icon button circle is-outline tooltip pinterest" href="https://pinterest.com/pin/create/button?url=https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/&amp;media=https://xmpro.com/wp-content/uploads/2023/09/MicrosoftTeams-image-48.png&amp;description=XMPro%20Suite%20on%20NVIDIA%20Cloud%20GPUs" onclick="window.open(this.href,this.title,'width=500,height=500,top=300px,left=300px'); return false;" rel="noopener nofollow" target="_blank" title="Pin on Pinterest"><i class="icon-pinterest"></i></a><a aria-label="Share on LinkedIn" class="icon button circle is-outline tooltip linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/&amp;title=XMPro%20Suite%20on%20NVIDIA%20Cloud%20GPUs" onclick="window.open(this.href,this.title,'width=500,height=500,top=300px,left=300px'); return false;" rel="noopener nofollow" target="_blank" title="Share on LinkedIn"><i class="icon-linkedin"></i></a></div></div></div>
<nav class="navigation-post" id="nav-below" role="navigation">
<div class="flex-row next-prev-nav bt bb">
<div class="flex-col flex-grow nav-prev text-left">

</div>

</div>
</nav>
</div>
</article>
<div class="comments-area" id="comments">
</div>

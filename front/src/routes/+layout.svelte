<script>
	import '../app.postcss';
	import { LightSwitch } from '@skeletonlabs/skeleton';
	import Navbar from '../components/navbar.svelte';

	// Highlight JS
	import hljs from 'highlight.js/lib/core';
	import 'highlight.js/styles/github-dark.css';
	import { storeHighlightJs } from '@skeletonlabs/skeleton';
	import xml from 'highlight.js/lib/languages/xml'; // for HTML
	import css from 'highlight.js/lib/languages/css';
	import javascript from 'highlight.js/lib/languages/javascript';
	import typescript from 'highlight.js/lib/languages/typescript';

	hljs.registerLanguage('xml', xml); // for HTML
	hljs.registerLanguage('css', css);
	hljs.registerLanguage('javascript', javascript);
	hljs.registerLanguage('typescript', typescript);
	storeHighlightJs.set(hljs);

	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });
</script>

<div>
	<div class="bg-primary-500">
		<div class="flex justify-between p-2">
			<div>
				<h3 class="h3 p-2"><a href="/">My bookshop</a></h3>
			</div>
			<div class="flex justify-center">
				<input class="input" title="Input (text)" type="text" placeholder="input text" />
				<LightSwitch />
			</div>
		</div>
	</div>
	<Navbar />
	<slot />
</div>

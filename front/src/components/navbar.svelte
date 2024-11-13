<script>
	import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
</script>

<nav class="bg-primary-300 h-14">
	<TabGroup
		justify="justify-center"
		active="variant-filled-primary"
		hover="hover:variant-soft-primary"
		flex="flex-1 lg:flex-none"
		rounded=""
		border=""
		class="bg-surface-100-800-token w-full"
	>
		<TabAnchor href="/">
			<svelte:fragment slot="lead">(icon)</svelte:fragment>
			<span>Book</span>
		</TabAnchor>
	</TabGroup>
</nav>

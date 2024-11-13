<script>
	import { LightSwitch } from "@skeletonlabs/skeleton";
</script>

<header class="bg-primary-500 py-4">
	<div class="container mx-auto flex justify-between items-center">
		<a href="/" class="text-2xl font-bold h3">My Bookshop</a>
		<div class="flex items-center gap-4">
			<input
				type="text"
				placeholder="Chercher un livre..."
				name="search"
				class="input"
			/>
			<button type="button" class="btn variant-filled-secondary">Trouver</button>
			<LightSwitch />
		</div>
	</div>
</header>

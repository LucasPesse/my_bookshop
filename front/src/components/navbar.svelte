<script>
	import { LightSwitch } from '@skeletonlabs/skeleton';
</script>

<header class="bg-primary-500 py-4">
	<div class="container mx-auto flex justify-between items-center">
		<a href="/" class="text-2xl font-bold h3">My Bookshop</a>
		<div class="flex items-center gap-4">
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
				<input type="search" placeholder="Cherchez un livre..." />
				<button class="variant-filled-secondary">Rechercher</button>
			</div>
			<LightSwitch />
		</div>
	</div>
</header>

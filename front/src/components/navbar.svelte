<script>
	export let connected;
	import { LightSwitch, Avatar } from '@skeletonlabs/skeleton';
	import { Dropdown, DropdownItem } from 'flowbite-svelte';
</script>

<header class="bg-primary-500 py-4">
	<div class="container mx-auto flex justify-between items-center">
		<a href="/" class="text-2xl font-bold h3">My Bookshop</a>
		<div class="flex items-center gap-4">
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
				<input type="search" placeholder="Cherchez un livre..." />
				<button class="variant-filled-secondary">Rechercher</button>
			</div>
			<Avatar initials="JD" background="bg-secondary-500 cursor-default" />
			<Dropdown>
				{#if connected}
					<DropdownItem href="/compte">Mon compte</DropdownItem>
				{:else}
					<DropdownItem href="/inscription">S'inscrire</DropdownItem>
					<DropdownItem href="/connexion">Se connecter</DropdownItem>
				{/if}
				<div class="flex justify-center">
					<LightSwitch />
				</div>
			</Dropdown>
		</div>
	</div>
</header>

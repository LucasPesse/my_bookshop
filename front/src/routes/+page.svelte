<script>
	import Promo from '$/components/promo.svelte';
	import LastArrival from '$/components/last_arrival.svelte';
	export let data;
</script>

<!-- Main Container -->
<div class="flex justify-center">
	<div class="bg-surface-50 dark:bg-surface-700 w-2/3 text-center">
		<Promo />
		<LastArrival books={data.books} />
	</div>
</div>

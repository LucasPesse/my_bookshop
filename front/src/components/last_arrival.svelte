<script>
	export let books;
</script>

<section class="py-12 container mx-auto">
	<h3 class="text-3xl font-semibold text-center mb-8">Livres en Vedette</h3>
	<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
		{#each books as book}
			<div class="bg-white rounded-lg shadow-lg overflow-hidden">
				<img src={book.cover} alt="Couverture de {book.title}" class="w-full h-64 object-cover" />
				<div class="p-4">
					<a
						href={`/${book.id}`}
						class="text-xl font-bold h-12 overflow-hidden text-ellipsis whitespace-nowrap dark:text-surface-900"
					>
						{book.title}
					</a>
					<p class="text-surface-800">{book.author}</p>
					<p class="text-surface-500 font-semibold">{book.price}</p>
					<button type="button" class="btn variant-filled-primary">Ajouter au panier</button>
				</div>
			</div>
		{/each}
	</div>
</section>

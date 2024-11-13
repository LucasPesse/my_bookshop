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
					<a href={`/${book.id}`} class="text-xl font-bold h-12 overflow-hidden text-ellipsis whitespace-nowrap">
						{book.title}
					</a>
					<p class="text-gray-600">{book.author}</p>
					<p class="text-blue-600 font-semibold">{book.price}</p>
					<button class="mt-4 w-full bg-blue-600 py-2 rounded hover:bg-blue-700">
						Ajouter au Panier
					</button>
				</div>
			</div>
		{/each}
	</div>
</section>

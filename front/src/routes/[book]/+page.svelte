<script>
	export let data;
	let book_id = data.id;
</script>

<main class="bg-gray-50 p-6 rounded-lg shadow-lg max-w-4xl mx-auto">
	<div class="flex flex-col md:flex-row items-center md:space-x-8">
		<img
			src={data.volumeInfo.imageLinks.large}
			alt={data.volumeInfo.title}
			class="w-48 h-72 object-cover rounded-md shadow-md"
		/>
		<div class="mt-6 md:mt-0">
			<h1 class="text-3xl font-semibold text-gray-900">{data.volumeInfo.title}</h1>
			<h2 class="text-xl text-gray-700 mt-2">par {data.volumeInfo.authors.join(', ')}</h2>
			<p class="text-gray-600 mt-4">{@html data.volumeInfo.description}</p>
			<div class="mt-6">
				<p class="text-lg font-medium text-gray-800">Éditeur : {data.volumeInfo.publisher}</p>
				<p class="text-sm text-gray-500">Publié le : {data.volumeInfo.publishedDate}</p>
				<p class="text-sm text-gray-500">Pages : {data.volumeInfo.pageCount}</p>
				<p class="text-sm text-gray-500">Catégories : {data.volumeInfo.categories.join(', ')}</p>
			</div>
			<div class="mt-6">
				{#if data.saleInfo.listPrice}
					<p class="text-lg font-medium text-gray-800">
						Prix : {data.saleInfo.listPrice.amount}
						{data.saleInfo.listPrice.currencyCode}
					</p>
				{:else}
					<p class="text-lg font-medium text-gray-800">
						Indisponible
					</p>
				{/if}
				<form method="post">
					<input type="hidden" name="book_id" bind:value={book_id}>
					<div class="py-2" min="1">
						<input type="number" name="quantity" value="1" class="input w-1/3">
					</div>
					<button
						type="submit"
						class="btn variant-filled-primary"
					>
						Acheter maintenant
					</button>
				</form>
			</div>
			<div class="mt-4">
				<a href={data.volumeInfo.previewLink} target="_blank" class="text-primary-600 hover:underline"
					>Aperçu du livre</a
				>
			</div>
		</div>
	</div>
</main>

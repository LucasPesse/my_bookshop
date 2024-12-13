<script>
	export let data;
</script>

<div class="p-8">
	<h3 class="text-2xl font-bold text-center mb-6">Votre panier</h3>
	<div class="flex justify-between gap-6">
		<!-- Cart Section -->
		<div class="bg-primary-500 w-2/3 p-5 rounded-lg shadow-md">
			<h4 class="text-xl font-semibold mb-4">Votre panier</h4>
			<div class="table-container">
				<table class="table table-compact table-hover">
					<thead>
						<tr>
							<th>Produit</th>
							<th>Quantité</th>
							<th>Prix</th>
							<th>Total</th>
						</tr>
					</thead>
					<tbody>
						{#each data.books as book}
							<tr>
								<td class="flex">
									<img
										src={book.cover}
										alt={book.title}
										class="w-20 h-28 object-cover mr-4 rounded-md"
									/>
									<div class="flex-1">
										<h5 class="text-lg font-semibold">{book.title}</h5>
										<p>{book.author}</p>
									</div>
								</td>
								<td>
                  <input type="number" class="input variant-form-material w-20" min="1" value="1" />
                </td>
								<td>
									{book.price} €
								</td>
								<td>{Number(book.price) * 2} €</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>

		<!-- Payment Section -->
		<div class="bg-secondary-500 w-1/3 p-5 rounded-lg shadow-md">
			<h4 class="text-xl font-semibold mb-4">Moyen de paiement</h4>
			<p class="text-gray-700">Veuillez choisir votre moyen de paiement.</p>
			<button class="mt-4 w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">
				Procéder au paiement
			</button>
		</div>
	</div>
</div>

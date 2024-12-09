<script>
	export let data, form;

	const order = {
		orders: [
			{
				id: 1,
				date: '2024-06-10',
				total: 45.5,
				status: 'Livrée',
				items: [
					{ title: 'Le Seigneur des Anneaux', author: 'J.R.R. Tolkien', quantity: 1, price: 25.5 },
					{ title: '1984', author: 'George Orwell', quantity: 1, price: 20 }
				]
			},
			{
				id: 2,
				date: '2024-05-15',
				total: 60,
				status: 'En cours de livraison',
				items: [{ title: 'Dune', author: 'Frank Herbert', quantity: 2, price: 30 }]
			}
		]
	};
</script>

<div>
	<div class="bg-surface-50 flex justify-center m-5 p-5 dark:bg-surface-900 rounded-lg">
		<h3 class="h3">Page de compte</h3>
	</div>
	<div class="flex justify-center">
		<form class="w-3/5 bg-surface-50 dark:bg-surface-900 m-5 rounded-lg" method="post">
			<h4 class="h4 p-5 text-center">Mes informations</h4>
			<div class="p-2">
				<h5 class="h5">Mes informations personnelles</h5>
				<hr />
				<div class="flex justify-center py-5">
					<div class="w-1/2">
						<p>Vous pouvez modifier vos informations</p>
					</div>
					<div class="w-1/2 flex justify-between">
						<label class="label">
							<div>
								<span>Prénom :</span>
							</div>
							<input
								type="text"
								name="fname"
								class="input variant-form-material"
								required
								value={data.user_info.first_name}
							/>
						</label>
						<label class="label">
							<div>
								<span>Nom :</span>
							</div>
							<input
								type="text"
								name="lname"
								class="input variant-form-material"
								required
								value={data.user_info.last_name}
							/>
						</label>
					</div>
				</div>

				<h5 class="h5">Mon adresse mail</h5>
				<hr />
				<div class="flex justify-center py-5">
					<div class="w-1/2">
						<p>
							Vous pouvez changer votre adresse mail, un nouveau mail de confirmation vous sera
							envoyé.
						</p>
					</div>
					<div class="w-1/2">
						<label class="label">
							<div>
								<span>Adresse email :</span>
							</div>
							<input
								type="email"
								name="email"
								class="input variant-form-material"
								required
								value={data.user_info.email}
								on:input={() => {
									form = null;
								}}
							/>
							{#if form?.invalid}
								<p class="text-error-500">{form?.invalid_msg}</p>
							{/if}
						</label>
					</div>
				</div>

				<h5 class="h5">Changer mon mot de passe</h5>
				<hr />
				<div class="flex justify-center py-5">
					<div class="w-1/2">
						<p>
							Votre mot de passe doit contenir huit caractères avec des chiffres et un caractère
							spécial
						</p>
					</div>
					<div class="w-1/2">
						<div class="flex justify-between">
							<label class="label">
								<div>
									<span>Mot de passe :</span>
								</div>
								<input
									type="password"
									name="password"
									class="input variant-form-material"
									on:input={() => {
										form = null;
									}}
								/>
							</label>
							<label class="label">
								<div>
									<span>Verification du mot de passe :</span>
								</div>
								<input type="password" name="password_verif" class="input variant-form-material" />
							</label>
						</div>
						{#if form?.incorrect}
							<p class="text-error-500">{form?.error}</p>
						{:else if form?.missmatch}
							<p class="text-error-500">{form?.message}</p>
						{/if}
					</div>
				</div>

				<h5 class="h5">S'abonner a la newsletter</h5>
				<hr />
				<label class="flex items-center space-x-2 py-5">
					<input
						class="checkbox"
						type="checkbox"
						name="newsletter"
						defaultChecked={data.user_info.newsletter}
					/>
					<p>
						Je souhaite recevoir les dernières sorties et les informations sur les événements à
						venir dans ma boutique.
					</p>
				</label>

				<div class="flex justify-end px-5">
					<input type="hidden" name="id" value={data.user_info.id} />
					<button type="submit" class="btn variant-soft-primary">Valider les changements</button>
				</div>
			</div>
		</form>
		<div class="w-2/5 bg-surface-50 dark:bg-surface-900 m-5 rounded-lg">
			<h4 class="h4 p-5 text-center">Commandes passées</h4>
			<div class="p-5 space-y-5">
				{#each order.orders as order}
					<div class="border rounded-lg p-4 bg-white dark:bg-gray-800 shadow-sm">
						<h5 class="h5 mb-2">Commande #{order.id}</h5>
						<p><strong>Date :</strong> {order.date}</p>
						<p><strong>Total :</strong> {order.total} €</p>
						<p><strong>Statut :</strong> {order.status}</p>
						<hr class="my-2" />
						<ul class="list-disc list-inside">
							{#each order.items as item}
								<li>
									<strong>{item.title}</strong> par {item.author} — {item.quantity} × {item.price} €
								</li>
							{/each}
						</ul>
					</div>
				{:else}
					<p>Aucune commande passée.</p>
				{/each}
			</div>
		</div>
	</div>
</div>

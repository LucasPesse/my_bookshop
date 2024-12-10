<script>
	export let data;
</script>

<div>
	<div class="bg-surface-50 flex justify-center m-5 p-5 dark:bg-surface-900 rounded-lg">
		<h3 class="h3">Page de compte</h3>
	</div>
	<div class="flex justify-center">
		<div class="w-3/5 bg-primary-500 m-5 rounded-lg">
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
								value={data.user_info.email}
							/>
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
					<div class="w-1/2 flex justify-between">
						<label class="label">
							<div>
								<span>Mot de passe :</span>
							</div>
							<input type="password" name="fname" class="input variant-form-material" />
						</label>
						<label class="label">
							<div>
								<span>Verification du mot de passe :</span>
							</div>
							<input type="password" name="lname" class="input variant-form-material" />
						</label>
					</div>
				</div>
				<p>newsletter</p>
			</div>
		</div>
		<div class="w-2/5 bg-secondary-500 m-5 rounded-lg">
			<h4 class="h4 p-5 text-center">Commandes passées</h4>
		</div>
	</div>
</div>

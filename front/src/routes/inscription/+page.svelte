<script>
	export let form;
	import { toast } from '@zerodevx/svelte-toast';

	if (form?.status == 200) {
		toast.push(
			`<strong>${form?.message}</strong><br>
	  Cliquez <a href="/">ici</a> pour revenir à l'accueil`,
			{
				theme: {
					'--toastColor': 'mintcream',
					'--toastBackground': 'rgba(72,187,120,0.9)',
					'--toastBarBackground': '#2F855A'
				}
			}
		);
	}
</script>

<div class="flex justify-center h-svh">
	<div class="w-1/2"></div>
	<div class="w-1/2 flex justify-center items-center">
		<form method="post" class="p-5">
			<h3 class="h3">Créez votre compte</h3>
			<p>
				Vous avez déjà un compte ? Vous pouvez vous connecter <a class="anchor" href="/connexion">ici</a> !
			</p>
			<div class="py-5 w-3/4">
				<label class="label py-2">
					<div>
						<span>Prénom</span>
					</div>
					<input type="text" name="first_name" class="input" placeholder="Ex : Jhon" required />
				</label>
				<label class="label py-2">
					<div>
						<span>Nom</span>
					</div>
					<input type="text" name="last_name" class="input" placeholder="Ex : Doe" required />
				</label>
				<label class="label py-2">
					<div>
						<span>Adresse email (valide)</span>
					</div>
					<input
						type="email"
						name="email"
						class="input"
						placeholder="Ex : jhon.doe@example.com"
						on:input={() => {
							form = null;
						}}
						required
					/>
					{#if form?.existing}
						<p class="text-error-500">{form?.mail_error}</p>
					{:else if form?.invalid}
						<p class="text-error-500">{form?.invalid_msg}</p>
					{/if}
				</label>
				<label class="label py-2">
					<div>
						<span>Mot de passe</span>
					</div>
					<input
						type="password"
						name="password"
						class="input"
						placeholder="Ex : ********"
						on:input={() => {
							form = null;
						}}
						required
					/>
					<div>
						<p class="text-sm">
							Votre mot de passe doit contenir huit caractères avec des chiffres et un caractère
							spécial
						</p>
						{#if form?.incorrect}
							<p class="text-error-500">{form?.error}</p>
						{/if}
					</div>
				</label>
				<label class="flex items-center space-x-2">
					<input class="checkbox" type="checkbox" name="newsletter" />
					<p>
						Je souhaite recevoir les dernières sorties et les informations sur les événements à
						venir dans ma boutique.
					</p>
				</label>
			</div>
			<button type="submit" class="btn variant-soft-primary">Créer son compte</button>
		</form>
	</div>
</div>

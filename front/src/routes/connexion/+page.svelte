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
	<div class="w-1/2 flex justify-center items-center">
		<form method="post" class="p-5">
			<h3 class="h3">Se connecter à son compte</h3>
			<div class="py-10">
				<label class="label py-2">
					<div>
						<span>Adresse email</span>
					</div>
					<input
						type="email"
						name="email"
						class="input"
						placeholder="Ex : jhon.doe@gmail.com"
						required
					/>
					{#if form?.invalid}
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
						required
					/>
				</label>
				<label class="flex items-center space-x-2">
					<input class="checkbox" type="checkbox" name="rememberMe" />
					<p>Se souvenir de moi.</p>
				</label>
			</div>
			{#if form?.existing == false}
				<p class="text-error-500">
					Adresse mail ou mot de passe incorrect, vous pouvez créer un compte <a
						class="anchor"
						href="/inscription">ici</a
					>
				</p>
			{/if}
			<button type="submit" class="btn variant-soft-primary">Se connecter</button>
		</form>
	</div>
	<div class="w-1/2"></div>
</div>

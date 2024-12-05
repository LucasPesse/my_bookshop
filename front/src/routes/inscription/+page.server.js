import { error, fail, redirect } from "@sveltejs/kit";
import * as User from "$lib/user.js";

export const actions = {
  default: async ({ request, cookies }) => {
    const data = await request.formData();
    const fname = data.get("first_name");
    const lname = data.get("last_name");
    const mail = data.get("email");
    const password = data.get("password");
    const newsletter = data.get("newsletter") ? true : false;

    // Password verification
    const regexp =
      /^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d)[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$/;
    if (!regexp.test(password))
      return fail(400, {
        incorrect: true,
        error: "Votre mot de passe ne correspond pas aux normes.",
      });

    // Verification of the existance of the mail
    const user_info = await User.find_user(mail);
    if (user_info != null)
      return fail(400, {
        existing: true,
        mail_error: "Un compte existe déjà avec cette adresse email.",
      });

    const user_data = await User.create_user(
      fname,
      lname,
      mail,
      password,
      newsletter,
    );
    if (user_data.status == 200) {
      cookies.set("user", user_data.id, { path: "/" });
      return {
        status: 200,
        message: "Compte créé avec succès !",
      };
    }
  },
};

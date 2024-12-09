import { error, fail } from "@sveltejs/kit";
import * as User from "$lib/user.js";

export async function load({ cookies }) {
  const user = cookies.get("user");

  if (!user) throw error(403, "Vous n'êtes pas connecté.");

  const data = await User.get_user_info(user);

  if (!data.data.user_info) throw error(403, "Vous n'êtes pas connecté.");

  return {
    user_info: data.data.user_info,
  };
}

export const actions = {
  default: async ({ request }) => {
    const user_info = await request.formData();
    const id = user_info.get("id");
    const fname = user_info.get("fname");
    const lname = user_info.get("lname");
    const mail = user_info.get("email");
    const password = user_info.get("password");
    const password_verif = user_info.get("password_verif");
    const newsletter = user_info.get("newsletter") ? true : false;

    if (password != "") {
      // Password match
      if (password != password_verif)
        return fail(400, {
          missmatch: true,
          message: "Les mots de passe divergent.",
        });

      // Password verification
      const regexp =
        /^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d)[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$/;
      if (!regexp.test(password))
        return fail(400, {
          incorrect: true,
          error: "Votre mot de passe ne correspond pas aux normes.",
        });
    }

    // Mail verification
    const mail_regex = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
    if (!mail_regex.test(mail))
      return fail(400, {
        invalid: true,
        invalid_msg: "Votre adresse mail n'est pas une adresse valide.",
      });

    const status = await User.edit_user(
      id,
      fname,
      lname,
      mail,
      password || false,
      newsletter,
    );
    if (status.status == 200) return;
  },
};

import * as User from "$lib/user.js";
import { fail } from "@sveltejs/kit";

export const actions = {
  default: async ({ cookies, request }) => {
    const info = await request.formData();
    const mail = info.get("email");
    const password = info.get("password");
    const remeber = info.get("rememberMe");

    const mail_regex = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
    if (!mail_regex.test(mail))
      return fail(400, {
        invalid: true,
        invalid_msg: "Votre adresse mail n'est pas une adresse valide.",
      });

    const user_id = await User.connect_user(mail, password);
    if (user_id.id == null)
      return fail(400, {
        existing: false,
      });
    cookies.set("user", user_id.id, { path: "/" });
    return {
      status: 200,
      message: "Connecté avec succès",
    };
  },
};

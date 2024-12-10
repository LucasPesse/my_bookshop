import { error } from "@sveltejs/kit";
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

import { error } from "@sveltejs/kit";

export async function load({ cookies }) {
  const user = cookies.get("user");

  if (!user) throw error(403);
}

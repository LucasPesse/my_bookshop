export async function load({ cookies }) {
  console.log(cookies.get("user"));
}

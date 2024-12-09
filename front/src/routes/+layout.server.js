export async function load({ cookies }) {
  const connected = cookies.get("user") ? true : false;
  return {
    connected: connected,
  };
}

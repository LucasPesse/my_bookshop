import * as Book from "$lib/books";

export async function load() {
  return await Book.get_books();
}

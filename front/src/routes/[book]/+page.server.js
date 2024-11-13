import * as Book from "$lib/books";

export async function load({ params }) {
  const book = await Book.get_a_book(params.book);
  return book;
}

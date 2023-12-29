import Image from "next/image";
import useSWR from "swr";

export default function Home() {
  const fetcher = (url: string) => fetch(url).then((res) => res.json());

  const { data, error } = useSWR("/api/2/3", fetcher);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      This is the home page
      {data && <div>{data}</div>}
    </main>
  );
}

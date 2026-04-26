import { useEffect, useState } from "react";
import API from "../services/api";

function ListPage() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("");
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let ignore = false;

    const fetchData = async () => {
      try {
        setLoading(true);

        const url = query
          ? `/api/search?q=${query}`
          : status
          ? `/api/status/${status}`
          : "/api/all";

        const res = await API.get(url);

        if (!ignore) {
          setData(res.data);
        }
      } catch (err) {
        console.error(err);
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    };

    fetchData();

    return () => {
      ignore = true;
    };
  }, [status, query]);

  const handleDelete = (id) => {
    if (!window.confirm("Delete this record?")) return;

    API.delete(`/api/${id}`)
      .then(() => {
        alert("Deleted!");
        setData((prev) => prev.filter((item) => item.id !== id));
      })
      .catch((err) => console.error(err));
  };

  const handleEdit = (item) => {
    const newName = prompt("Company Name:", item.companyName);
    if (!newName) return;

    const newScore = prompt("Score:", item.complianceScore);
    const newStatus = prompt(
      "Status (COMPLIANT/NON-COMPLIANT):",
      item.status
    );

    const payload = {
      companyName: newName,
      complianceScore: newScore ? Number(newScore) : null,
      status: newStatus,
      description: item.description,
    };

    API.put(`/api/${item.id}`, payload)
      .then(() => {
        alert("Updated!");
        setData((prev) =>
          prev.map((it) =>
            it.id === item.id ? { ...it, ...payload } : it
          )
        );
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Compliance Records</h1>

      {/* ✅ ADD BUTTON (FIXED POSITION) */}
      <button
        onClick={() => (window.location.href = "/add")}
        className="bg-blue-500 text-white px-3 py-2 mb-4"
      >
        Add Record
      </button>

      {/* SEARCH */}
      <input
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-2 mb-4"
      />

      {/* FILTER */}
      <select
        onChange={(e) => setStatus(e.target.value)}
        className="mb-4 border p-2"
      >
        <option value="">All</option>
        <option value="COMPLIANT">Compliant</option>
        <option value="NON-COMPLIANT">Non-Compliant</option>
      </select>

      {loading ? (
        <p>Loading...</p>
      ) : data.length === 0 ? (
        <p>No records found</p>
      ) : (
        <table className="table-auto border w-full">
          <thead>
            <tr>
              <th className="border px-4">ID</th>
              <th className="border px-4">Company</th>
              <th className="border px-4">Score</th>
              <th className="border px-4">Status</th>
              <th className="border px-4">Actions</th>
            </tr>
          </thead>

          <tbody>
            {data.map((item) => (
              <tr key={item.id}>
                <td className="border px-4">{item.id}</td>
                <td className="border px-4">{item.companyName}</td>
                <td className="border px-4">{item.complianceScore}</td>
                <td className="border px-4">{item.status}</td>

                <td className="border px-4 space-x-2">
                  <button
                    onClick={() => handleEdit(item)}
                    className="bg-yellow-500 text-white px-2 py-1"
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(item.id)}
                    className="bg-red-500 text-white px-2 py-1"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ListPage;
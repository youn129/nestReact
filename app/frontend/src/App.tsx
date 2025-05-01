import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import SignUp from "./SignUp";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [auctionItems, setAuctionItems] = useState<any[]>([]);
  const [query, setQuery] = useState<string>("laptop");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const fetchAuctionItems = async (searchQuery: string) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/auctions/fetch-auctions?query=${searchQuery}&popular=true`
      );

      const result = await response.json();
      console.log("🔄 API Response:", result);

      if (Array.isArray(result.data)) {
        setAuctionItems(result.data);
      } else {
        console.warn("Unexpected response format:", result);
        setAuctionItems([]);
      }
    } catch (error) {
      console.error("Error fetching auction data:", error);
      setError("Failed to fetch auction items.");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchAuctionItems(query);
  }, []);

  useEffect(() => {
    console.log("Current auctionItems:", auctionItems);
  }, [auctionItems]);

  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              Auction App
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="btn btn-primary me-2" to="/signup">
                    Sign Up
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="btn btn-secondary me-2" to="/login">
                    Login
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route
            path="/"
            element={
              <div>
                <h1>Welcome to the Auction Platform</h1>
                <div className="search-bar">
                  <input
                    type="text"
                    placeholder="Search for items"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    className="form-control w-50 my-3"
                  />
                  <button
                    onClick={() => fetchAuctionItems(query)}
                    className="btn btn-primary"
                  >
                    Search
                  </button>
                </div>

                {isLoading && <p>Loading...</p>}
                {error && <p className="text-danger">{error}</p>}

                <section>
                  <h2>Auction Items</h2>
                  {Array.isArray(auctionItems) && auctionItems.length > 0 ? (
                    <ul className="list-group">
                      {auctionItems.map((item) => (
                        <li
                          key={item.itemId}
                          className="list-group-item d-flex align-items-center"
                        >
                          <img
                            src={item.image?.imageUrl}
                            alt={item.title}
                            width="100"
                            className="me-3"
                          />
                          <div>
                            <h5>{item.title}</h5>
                            <p>Price: ${item.price?.value}</p>
                          </div>
                        </li>
                      ))}
                    </ul>
                  ) : (
                    !isLoading && <p>No auction items available.</p>
                  )}
                </section>
              </div>
            }
          />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

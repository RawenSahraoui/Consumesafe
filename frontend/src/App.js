import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

function App() {
  const [productName, setProductName] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [alternatives, setAlternatives] = useState([]);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await axios.get(`${API_URL}/categories`);
      setCategories(response.data.categories);
    } catch (error) {
      console.error('Erreur lors du chargement des catégories:', error);
    }
  };

  const checkProduct = async (e) => {
    e.preventDefault();
    if (!productName.trim()) return;

    setLoading(true);
    setResult(null);
    setAlternatives([]);

    try {
      const response = await axios.post(`${API_URL}/check-product`, {
        product_name: productName
      });
      setResult(response.data);
    } catch (error) {
      console.error('Erreur:', error);
      setResult({ error: 'Erreur lors de la vérification du produit' });
    } finally {
      setLoading(false);
    }
  };

  const fetchAlternatives = async (category) => {
    setSelectedCategory(category);
    try {
      const response = await axios.get(`${API_URL}/alternatives/${category}`);
      setAlternatives(response.data.alternatives);
    } catch (error) {
      console.error('Erreur:', error);
      setAlternatives([]);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>ConsumeSafe</h1>
        <p className="subtitle">Vérifiez si un produit est boycotté et trouvez des alternatives tunisiennes</p>
      </header>

      <main className="container">
        <section className="search-section">
          <form onSubmit={checkProduct}>
            <div className="input-group">
              <input
                type="text"
                value={productName}
                onChange={(e) => setProductName(e.target.value)}
                placeholder="Entrez le nom d'un produit (ex: Coca Cola)"
                className="search-input"
              />
              <button type="submit" className="search-button" disabled={loading}>
                {loading ? 'Vérification...' : 'Vérifier'}
              </button>
            </div>
          </form>

          {result && !result.error && (
            <div className={`result-card ${result.is_boycotted ? 'boycotted' : 'safe'}`}>
              <h2>{result.product_name}</h2>
              {result.is_boycotted ? (
                <>
                  <div className="status boycott">
                    <span>PRODUIT BOYCOTTÉ</span>
                  </div>
                  <p className="reason"><strong>Raison:</strong> {result.reason}</p>
                  
                  {result.alternatives && result.alternatives.length > 0 && (
                    <div className="alternatives-box">
                      <h3>Alternatives tunisiennes recommandées:</h3>
                      <ul>
                        {result.alternatives.map((alt, index) => (
                          <li key={index}>{alt}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </>
              ) : (
                <div className="status safe">
                  <span>PRODUIT NON BOYCOTTÉ</span>
                </div>
              )}
            </div>
          )}

          {result && result.error && (
            <div className="result-card error">
              <p>{result.error}</p>
            </div>
          )}
        </section>

        <section className="categories-section">
          <h2>Produits Tunisiens par Catégorie</h2>
          <div className="categories-grid">
            {categories.map((category) => (
              <button
                key={category}
                className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
                onClick={() => fetchAlternatives(category)}
              >
                {category.charAt(0).toUpperCase() + category.slice(1)}
              </button>
            ))}
          </div>

          {alternatives.length > 0 && (
            <div className="alternatives-list">
              <h3>Produits disponibles - {selectedCategory}</h3>
              <div className="products-grid">
                {alternatives.map((product, index) => (
                  <div key={index} className="product-card">
                    <h4>{product.name}</h4>
                    <p className="product-type">{product.type}</p>
                    <p className="product-origin">Origine: {product.origin}</p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </section>
      </main>

      <footer className="footer">
        <p>ConsumeSafe 2024 - Made for Tunisia</p>
      </footer>
    </div>
  );
}

export default App;
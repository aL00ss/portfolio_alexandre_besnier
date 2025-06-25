import { h } from 'preact';
import { useState, useEffect, useMemo } from 'preact/hooks';
import Fuse from 'fuse.js';

export default function Search({ items }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  // On conserve l’instance Fuse entre les renders
  const fuse = useMemo(() => {
    return new Fuse(items, {
      keys: ['tags'],
      threshold: 0.3,
    });
  }, [items]);

  useEffect(() => {
    if (query.trim().length > 0) {
      // ✂️ Correction : espace manquant, et nommage plus clair
      const fuseResults = fuse.search(query).map(r => r.item);
      setResults(fuseResults);
    } else {
      setResults([]);
    }
  }, [query, fuse]);

  return (
    <div class="search-container">
      <input
        class="search-input"
        type="text"
        placeholder="Rechercher par tag…"
        value={query}
        onInput={e => setQuery(e.target.value)}
      />
      {results.length > 0 && (
        <ul class="search-results">
          {results.map(item => (
            <li key={item.slug}>
              <a href={`/work/${item.slug}`}>{item.title}</a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

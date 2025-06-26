import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';

// Essayons d'instancier l'intégration
let preactIntegration;
try {
  preactIntegration = preact();
  // Si on a bien un objet d’intégration avec un nom, on logge
  if (preactIntegration && preactIntegration.name) {
    console.log(`🔌 Loaded integration: ${preactIntegration.name}`);
  } else {
    console.warn('⚠️ L’intégration Preact a été importée mais son nom est introuvable');
  }
} catch (e) {
  console.error('❌ Erreur lors de l’import de @astrojs/preact:', e);
}

// Export de la config avec l’intégration (ou vide si échec)
export default defineConfig({
  integrations: preactIntegration ? [preactIntegration] : [],
});

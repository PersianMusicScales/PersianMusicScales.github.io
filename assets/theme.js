try {
  const theme = localStorage.getItem('pms-theme');
  if (theme === 'dark' || theme === 'light') document.documentElement.dataset.theme = theme;
} catch {}

export const siteConfig = {
  title: 'Unreal 90分授業',
  logoText: 'Unreal 90分授業',
  githubRepo: 'metyatech/open-campus-unreal-90min',
  projectLink: 'https://github.com/metyatech/open-campus-unreal-90min',
  docsRepositoryBase:
    'https://github.com/metyatech/open-campus-unreal-90min/tree/main',
  description: 'オープンキャンパス向け Unreal Engine 90分体験授業教材',
  faviconHref: '/img/favicon.svg',
  adminMode: {
    publicFallbackPath: '/docs/intro',
    protectedLinks: [
      { href: '/docs/teacher-guide', label: '教員ガイド' },
      { href: '/docs/setup-and-troubleshooting', label: 'セットアップ・トラブル対応' },
    ],
  },
} as const;

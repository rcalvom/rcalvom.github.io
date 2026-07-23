export const site = {
  name: "Ricardo Calvo Mendez",
  description: "Ricardo Calvo Mendez's academic portfolio",
  url: "https://rcalvom.github.io",
  blogEnabled: true,
  email: "rcalvome@purdue.edu",
  location: "West Lafayette, IN",
  role: "PhD Student in ECE at Purdue University",
  institution: "Purdue University",
  links: {
    scholar: "https://scholar.google.com/citations?user=JwpDnSIAAAAJ&hl=es&authuser=1",
    orcid: "https://orcid.org/0009-0003-6681-4840",
    github: "https://github.com/rcalvom",
    linkedin: "https://www.linkedin.com/in/ricardo-calvo/"
  }
} as const;

type NavigationItem = {
  label: string;
  href: string;
  feature?: "blog";
};

export const navigation: readonly NavigationItem[] = [
  { label: "Publications", href: "/publications/" },
  { label: "Talks", href: "/talks/" },
  { label: "Blog Posts", href: "/year-archive/", feature: "blog" },
  { label: "CV", href: "/cv/" },
  { label: "About me", href: "/about-me/" }
];

export function visibleNavigation() {
  return navigation.filter((item) => item.feature !== "blog" || site.blogEnabled);
}

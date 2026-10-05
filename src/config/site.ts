export const site = {
  name: "Ricardo Andrés Calvo Méndez",
  description:
    "PhD student in Electrical and Computer Engineering at Purdue University working on formal verification, program analysis, and automated software testing.",
  url: "https://rcalvom.github.io",
  blogEnabled: false,
  email: "rcalvome@purdue.edu",
  location: "West Lafayette, IN",
  role: "PhD Student in ECE at Purdue University",
  institution: "Purdue University",
  cv: "/files/cv.pdf",
  resume: "/files/resume.pdf",
  /**
   * Availability banner shown in the home hero. Set `seeking` to false once the
   * search is over; nothing else needs to change.
   */
  availability: {
    seeking: true,
    term: "Summer 2027",
    kind: "research and software engineering internships"
  },
  links: {
    scholar: "https://scholar.google.com/citations?user=JwpDnSIAAAAJ",
    orcid: "https://orcid.org/0009-0003-6681-4840",
    dblp: "https://dblp.org/pid/355/2654",
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

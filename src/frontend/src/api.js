const API_BASE_URL =
  process.env.REACT_APP_API_URL || 'http://localhost:8000'

const fetchJson = async (path) => {
  const response = await fetch(`${API_BASE_URL}${path}`)

  if (!response.ok) {
    throw new Error(`Request failed for ${path} with status ${response.status}`)
  }

  return response.json()
}

const fetchAuthedJson = async (path, token) => {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })

  if (!response.ok) {
    throw new Error(`Request failed for ${path} with status ${response.status}`)
  }

  return response.json()
}

const postJson = async (path, body, token) => {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify(body),
  })

  if (!response.ok) {
    const errorText = await response.text()
    throw new Error(errorText || `Request failed for ${path} with status ${response.status}`)
  }

  return response.json()
}

const loginAdmin = async ({ email, password }) => {
  const formBody = new URLSearchParams()
  formBody.set('username', email)
  formBody.set('password', password)

  const response = await fetch(`${API_BASE_URL}/auth/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formBody.toString(),
  })

  if (!response.ok) {
    const errorText = await response.text()
    throw new Error(errorText || 'Invalid admin credentials')
  }

  return response.json()
}

const adminEndpoints = {
  profile: '/admin/create_profile',
  project: '/admin/create_project',
  competence: '/admin/create_competence',
  formation: '/admin/create_formation',
  outil: '/admin/create_outil',
  loisir: '/admin/create_loisir',
  langage: '/admin/create_langage',
}

const createAdminRecord = async (resource, payload, token) => {
  const endpoint = adminEndpoints[resource]

  if (!endpoint) {
    throw new Error(`Unknown admin resource: ${resource}`)
  }

  return postJson(endpoint, payload, token)
}

const updateAdminRecord = async (resource, id, payload, token) => {
  const endpoint = `/admin/update/${resource}/${id}`

  return postJson(endpoint, payload, token)
}

const deleteAdminRecord = async (resource, id, token) => {
  const response = await fetch(`${API_BASE_URL}/admin/delete/${resource}/${id}`, {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })

  if (!response.ok) {
    const errorText = await response.text()
    throw new Error(errorText || `Request failed for ${resource}/${id} with status ${response.status}`)
  }

  return response.json()
}

const adminListEndpoints = {
  profile: '/admin/profiles',
  project: '/admin/projects',
  competence: '/admin/competences',
  formation: '/admin/formations',
  outil: '/admin/outils',
  loisir: '/admin/loisirs',
  langage: '/admin/langages',
}

const loadAdminResources = async (token) => {
  const entries = await Promise.all(
    Object.entries(adminListEndpoints).map(async ([resource, path]) => [
      resource,
      await fetchAuthedJson(path, token),
    ])
  )

  return Object.fromEntries(entries)
}

const formatDate = (value) => {
  if (!value) return ''

  const date = new Date(value)
  if (Number.isNaN(date.getTime())) return value

  return new Intl.DateTimeFormat('fr-FR', {
    month: 'short',
    year: 'numeric',
  }).format(date)
}

const formatDateRange = (startDate, endDate) => {
  const start = formatDate(startDate)
  const end = formatDate(endDate)

  if (start && end) return `${start} - ${end}`
  if (start) return `Depuis ${start}`
  if (end) return end

  return ''
}

const resolveAssetUrl = (value) => {
  if (!value) return ''
  if (value.startsWith('http') || value.startsWith('data:')) return value
  if (value.startsWith('/')) return `${API_BASE_URL}${value}`

  return `${process.env.PUBLIC_URL}/images/${value}`
}

const buildLabel = (...parts) => parts.filter(Boolean).join(' · ')

const normalizePortfolio = ({
  profiles,
  projects,
  competences,
  formations,
  outils,
  loisirs,
  langages,
}) => {
  const profile = profiles[0] || {}
  const fullName = [profile.prenom, profile.nom].filter(Boolean).join(' ').trim()
  const primaryFormation = formations[0]

  const header = {
    homepage: '#top',
    title: fullName || 'Portfolio',
  }

  const about = {
    name: fullName || 'Portfolio',
    role: primaryFormation?.niveau || 'Développeur web',
    picture: resolveAssetUrl(profile.photo),
    description:
      profile.bio ||
      'Portfolio alimenté par le backend FastAPI de ce projet.',
    resume: '',
    social: {
      linkedin: profile.linkedin || '',
      github: profile.github || '',
    },
  }

  const projectCards = projects.map((project) => ({
    id: project.id,
    name: project.name,
    description: project.description,
    stack: [
      buildLabel(project.role),
      formatDateRange(project.date_debut, project.date_fin),
    ].filter(Boolean),
    sourceCode: project.url || '',
    livePreview: project.url || '',
    image: '',
  }))

  const skillGroups = {
    competences: competences.map((item) =>
      buildLabel(item.name, item.categorie_comp)
    ),
    langages: langages.map((item) => buildLabel(item.name, item.niveau)),
    outils: outils.map((item) =>
      buildLabel(item.name, item.categorie, item.niveau ? `${item.niveau}/10` : '')
    ),
  }

  const education = formations.map((item) => ({
    id: item.id,
    title: item.nom_formation,
    subtitle: item.nom_ecole,
    description: buildLabel(item.niveau, item.secteur),
    meta: formatDateRange(item.date_debut, item.date_fin),
  }))

  const interests = loisirs.map((item) => ({
    id: item.id,
    title: item.name,
    description: item.description,
  }))

  const contact = {
    email: profile.email || '',
    phone: profile.telephone || '',
    address: profile.adresse || '',
  }

  return {
    header,
    about,
    projects: projectCards,
    skills: skillGroups,
    education,
    interests,
    contact,
  }
}

export const loadPortfolio = async () => {
  const [profiles, projects, competences, formations, outils, loisirs, langages] =
    await Promise.all([
      fetchJson('/data/profiles'),
      fetchJson('/data/projects'),
      fetchJson('/data/competences'),
      fetchJson('/data/formations'),
      fetchJson('/data/outils'),
      fetchJson('/data/loisirs'),
      fetchJson('/data/langages'),
    ])

  return normalizePortfolio({
    profiles,
    projects,
    competences,
    formations,
    outils,
    loisirs,
    langages,
  })
}

export {
  resolveAssetUrl,
  formatDateRange,
  loginAdmin,
  createAdminRecord,
  updateAdminRecord,
  deleteAdminRecord,
  loadAdminResources,
}
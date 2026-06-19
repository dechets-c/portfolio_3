import { useEffect, useState } from 'react'
import {
  createAdminRecord,
  deleteAdminRecord,
  loadAdminResources,
  loginAdmin,
  updateAdminRecord,
} from '../../api'
import './Admin.css'

const authInitialState = {
  email: '',
  password: '',
}

const adminConfigs = [
  {
    key: 'profile',
    label: 'Profile',
    fields: [
      { name: 'prenom', label: 'Prénom', type: 'text', required: true },
      { name: 'nom', label: 'Nom', type: 'text', required: true },
      { name: 'email', label: 'Email', type: 'email', required: true },
      { name: 'telephone', label: 'Téléphone', type: 'tel', required: true },
      { name: 'adresse', label: 'Adresse', type: 'text', required: true },
      { name: 'dn', label: 'Date de naissance', type: 'datetime-local', required: true },
      { name: 'linkedin', label: 'LinkedIn', type: 'url', required: true },
      { name: 'github', label: 'GitHub', type: 'url', required: true },
      { name: 'photo', label: 'Photo', type: 'url', required: true },
      { name: 'bio', label: 'Bio', type: 'textarea', required: true },
    ],
  },
  {
    key: 'project',
    label: 'Project',
    fields: [
      { name: 'name', label: 'Nom', type: 'text', required: true },
      { name: 'description', label: 'Description', type: 'textarea', required: true },
      {
        name: 'role',
        label: 'Rôle',
        type: 'select',
        required: true,
        options: ['Développeur', 'Data scientist', 'Data engineer', 'Data analyst'],
      },
      { name: 'date_debut', label: 'Date de début', type: 'date', required: true },
      { name: 'date_fin', label: 'Date de fin', type: 'date', required: false },
      { name: 'url', label: 'URL', type: 'url', required: false },
    ],
  },
  {
    key: 'competence',
    label: 'Competence',
    fields: [
      { name: 'name', label: 'Nom', type: 'text', required: true },
      { name: 'niveau', label: 'Niveau', type: 'number', required: true },
      {
        name: 'categorie_comp',
        label: 'Catégorie',
        type: 'select',
        required: true,
        options: ['Statistiques', 'Développement', 'Data', 'Informatique', 'Soft Skills'],
      },
      {
        name: 'date_debut_comp',
        label: 'Date de début',
        type: 'datetime-local',
        required: true,
      },
    ],
  },
  {
    key: 'formation',
    label: 'Formation',
    fields: [
      { name: 'nom_formation', label: 'Formation', type: 'text', required: true },
      { name: 'nom_ecole', label: 'École', type: 'text', required: true },
      {
        name: 'niveau',
        label: 'Niveau',
        type: 'select',
        required: true,
        options: ['Bac', 'Bac +3', 'Bac +5'],
      },
      {
        name: 'secteur',
        label: 'Secteur',
        type: 'select',
        required: true,
        options: ['Informatique', 'Data'],
      },
      { name: 'date_debut', label: 'Date de début', type: 'datetime-local', required: true },
      { name: 'date_fin', label: 'Date de fin', type: 'datetime-local', required: false },
    ],
  },
  {
    key: 'outil',
    label: 'Outil',
    fields: [
      { name: 'name', label: 'Nom', type: 'text', required: true },
      { name: 'categorie', label: 'Catégorie', type: 'text', required: true },
      { name: 'niveau', label: 'Niveau', type: 'number', required: true },
      { name: 'url_logo', label: 'Logo', type: 'url', required: false },
    ],
  },
  {
    key: 'loisir',
    label: 'Loisir',
    fields: [
      { name: 'name', label: 'Nom', type: 'text', required: true },
      { name: 'description', label: 'Description', type: 'textarea', required: true },
    ],
  },
  {
    key: 'langage',
    label: 'Langage',
    fields: [
      { name: 'name', label: 'Nom', type: 'text', required: true },
      {
        name: 'niveau',
        label: 'Niveau',
        type: 'select',
        required: true,
        options: [
          'A1 - Débutant',
          'A2 - Élémentaire',
          'B1 - Intermédiaire',
          'B2 - Intermédiaire ++',
          'C1 - Avancé',
          'C2 - Maitrise',
          'Langue maternelle',
        ],
      },
    ],
  },
]

const createEmptyValues = (configs) =>
  Object.fromEntries(
    configs.map((config) => [
      config.key,
      Object.fromEntries(config.fields.map((field) => [field.name, ''])),
    ])
  )

const createEmptyRecords = (configs) =>
  Object.fromEntries(configs.map((config) => [config.key, []]))

const initialFormState = createEmptyValues(adminConfigs)

const getConfig = (resourceKey) =>
  adminConfigs.find((config) => config.key === resourceKey)

const normalizePayload = (values, fields) =>
  Object.fromEntries(
    fields.flatMap((field) => {
      const value = values[field.name]

      if (value === '' || value === null || value === undefined) {
        return field.required ? [[field.name, value]] : []
      }

      if (field.type === 'number') {
        return [[field.name, Number(value)]]
      }

      if (field.type === 'date') {
        return [[field.name, `${value}T00:00:00`]]
      }

      if (field.type === 'datetime-local') {
        return [[field.name, `${value}:00`]]
      }

      return [[field.name, value]]
    })
  )

const toInputValue = (field, value) => {
  if (value === null || value === undefined) {
    return ''
  }

  if (field.type === 'date') {
    return String(value).slice(0, 10)
  }

  if (field.type === 'datetime-local') {
    return String(value).replace('Z', '').slice(0, 16)
  }

  return String(value)
}

const formatDisplayValue = (field, value) => {
  if (value === null || value === undefined || value === '') {
    return '—'
  }

  if (field.type === 'date' || field.type === 'datetime-local') {
    const date = new Date(value)
    if (!Number.isNaN(date.getTime())) {
      return date.toLocaleDateString('fr-FR')
    }
  }

  return String(value)
}

const renderFieldControl = (field, value, onChange) => {
  if (field.type === 'textarea') {
    return (
      <textarea
        id={field.name}
        name={field.name}
        value={value}
        onChange={onChange}
        required={field.required}
        rows='4'
      />
    )
  }

  if (field.type === 'select') {
    return (
      <select
        id={field.name}
        name={field.name}
        value={value}
        onChange={onChange}
        required={field.required}
      >
        <option value=''>Sélectionner</option>
        {field.options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    )
  }

  return (
    <input
      id={field.name}
      name={field.name}
      type={field.type}
      value={value}
      onChange={onChange}
      required={field.required}
    />
  )
}

const Field = ({ field, value, onChange }) => (
  <label className='admin__field' htmlFor={field.name}>
    <span>{field.label}</span>
    {renderFieldControl(field, value, onChange)}
  </label>
)

const RecordSummary = ({ config, item }) => {
  const primaryField = config.fields[0]
  const secondaryField = config.fields[1]

  return (
    <div className='admin__record-summary'>
      <h4>{item[primaryField.name] || `${config.label} #${item.id}`}</h4>
      {secondaryField ? <p>{formatDisplayValue(secondaryField, item[secondaryField.name])}</p> : null}
    </div>
  )
}

const RecordDetails = ({ config, item }) => (
  <dl className='admin__record-details'>
    {config.fields.map((field) => (
      <div key={field.name}>
        <dt>{field.label}</dt>
        <dd>{formatDisplayValue(field, item[field.name])}</dd>
      </div>
    ))}
  </dl>
)

const RecordEditor = ({ config, item, onSave, onCancel }) => {
  const [values, setValues] = useState(
    config.fields.reduce((accumulator, field) => {
      accumulator[field.name] = toInputValue(field, item[field.name])
      return accumulator
    }, {})
  )

  const handleSubmit = (event) => {
    event.preventDefault()
    onSave(normalizePayload(values, config.fields))
  }

  return (
    <div className='admin__edit-panel'>
      <h4>
        Modifier {config.label.toLowerCase()} #{item.id}
      </h4>
      <form className='admin__form' onSubmit={handleSubmit}>
        {config.fields.map((field) => (
          <Field
            key={field.name}
            field={field}
            value={values[field.name]}
            onChange={(event) =>
              setValues((current) => ({ ...current, [field.name]: event.target.value }))
            }
          />
        ))}

        <div className='admin__record-actions'>
          <button type='submit' className='btn btn--outline'>
            Sauvegarder
          </button>
          <button type='button' className='btn btn--plain' onClick={onCancel}>
            Annuler
          </button>
        </div>
      </form>
    </div>
  )
}

const Admin = () => {
  const [credentials, setCredentials] = useState(authInitialState)
  const [token, setToken] = useState(() => localStorage.getItem('portfolio_admin_token') || '')
  const [adminEmail, setAdminEmail] = useState(() => localStorage.getItem('portfolio_admin_email') || '')
  const [forms, setForms] = useState(initialFormState)
  const [records, setRecords] = useState(() => createEmptyRecords(adminConfigs))
  const [editingRecord, setEditingRecord] = useState(() => createEmptyRecords(adminConfigs))
  const [status, setStatus] = useState('')
  const [error, setError] = useState('')
  const [submittingKey, setSubmittingKey] = useState('')
  const [loadingRecords, setLoadingRecords] = useState(false)

  useEffect(() => {
    if (token) {
      localStorage.setItem('portfolio_admin_token', token)
    } else {
      localStorage.removeItem('portfolio_admin_token')
    }

    if (adminEmail) {
      localStorage.setItem('portfolio_admin_email', adminEmail)
    } else {
      localStorage.removeItem('portfolio_admin_email')
    }
  }, [token, adminEmail])

  useEffect(() => {
    const loadData = async () => {
      if (!token) {
        return
      }

      setLoadingRecords(true)

      try {
        const data = await loadAdminResources(token)
        setRecords(data)
      } catch (loadError) {
        setError(loadError.message || 'Impossible de charger les données admin.')
      } finally {
        setLoadingRecords(false)
      }
    }

    loadData()
  }, [token])

  const isAuthenticated = Boolean(token)

  const handleCredentialChange = (event) => {
    const { name, value } = event.target
    setCredentials((current) => ({ ...current, [name]: value }))
  }

  const handleFieldChange = (resourceKey, fieldName, value) => {
    setForms((current) => ({
      ...current,
      [resourceKey]: {
        ...current[resourceKey],
        [fieldName]: value,
      },
    }))
  }

  const resetForm = (resourceKey) => {
    const config = getConfig(resourceKey)
    if (!config) {
      return
    }

    setForms((current) => ({
      ...current,
      [resourceKey]: Object.fromEntries(config.fields.map((field) => [field.name, ''])),
    }))
  }

  const refreshRecords = async () => {
    const data = await loadAdminResources(token)
    setRecords(data)
  }

  const handleAuthSubmit = async (event) => {
    event.preventDefault()
    setStatus('')
    setError('')

    try {
      const response = await loginAdmin(credentials)
      setToken(response.access_token)
      setAdminEmail(credentials.email)
      setStatus('Connexion réussie.')
    } catch (authError) {
      setError(authError.message || 'Connexion impossible.')
    }
  }

  const handleLogout = () => {
    setToken('')
    setAdminEmail('')
    setStatus('Déconnecté.')
    setError('')
  }

  const handleCreate = async (resourceKey) => {
    const config = getConfig(resourceKey)
    if (!config) {
      return
    }

    setSubmittingKey(resourceKey)
    setStatus('')
    setError('')

    try {
      const payload = normalizePayload(forms[resourceKey], config.fields)
      await createAdminRecord(resourceKey, payload, token)
      await refreshRecords()
      setStatus(`${config.label} ajouté avec succès.`)
      resetForm(resourceKey)
    } catch (submitError) {
      setError(submitError.message || `Impossible de créer ${config.label.toLowerCase()}.`)
    } finally {
      setSubmittingKey('')
    }
  }

  const handleDelete = async (resourceKey, itemId) => {
    setStatus('')
    setError('')

    try {
      await deleteAdminRecord(resourceKey, itemId, token)
      await refreshRecords()
      setStatus('Enregistrement supprimé.')
    } catch (deleteError) {
      setError(deleteError.message || 'Impossible de supprimer cet enregistrement.')
    }
  }

  const handleEditStart = (resourceKey, itemId) => {
    setEditingRecord((current) => ({
      ...current,
      [resourceKey]: itemId,
    }))
  }

  const handleEditCancel = (resourceKey) => {
    setEditingRecord((current) => ({
      ...current,
      [resourceKey]: null,
    }))
  }

  const handleEditSave = async (resourceKey, itemId, payload) => {
    setStatus('')
    setError('')

    try {
      await updateAdminRecord(resourceKey, itemId, payload, token)
      await refreshRecords()
      handleEditCancel(resourceKey)
      setStatus('Enregistrement mis à jour.')
    } catch (updateError) {
      setError(updateError.message || 'Impossible de mettre à jour cet enregistrement.')
    }
  }

  return (
    <section id='admin' className='section admin'>
      <h2 className='section__title'>Admin</h2>

      <div className='admin__intro'>
        <p>Connexion requise pour ajouter, modifier ou supprimer des données au backend.</p>
        <p>Les formulaires alimentent PostgreSQL via l’API FastAPI.</p>
      </div>

      {!isAuthenticated ? (
        <div className='admin__auth-card'>
          <h3 className='admin__card-title'>Connexion admin</h3>
          <form className='admin__form' onSubmit={handleAuthSubmit}>
            <label className='admin__field' htmlFor='email'>
              <span>Email</span>
              <input
                id='email'
                name='email'
                type='email'
                value={credentials.email}
                onChange={handleCredentialChange}
                required
              />
            </label>

            <label className='admin__field' htmlFor='password'>
              <span>Mot de passe</span>
              <input
                id='password'
                name='password'
                type='password'
                value={credentials.password}
                onChange={handleCredentialChange}
                required
              />
            </label>

            <button type='submit' className='btn btn--outline admin__submit'>
              Se connecter
            </button>
          </form>
        </div>
      ) : (
        <div className='admin__status-bar'>
          <div>
            <strong>Connecté</strong>
            <p>{adminEmail}</p>
          </div>
          <button type='button' className='btn btn--plain' onClick={handleLogout}>
            Déconnexion
          </button>
        </div>
      )}

      {(status || error) && (
        <div className={`admin__notice ${error ? 'admin__notice--error' : 'admin__notice--success'}`}>
          {error || status}
        </div>
      )}

      {isAuthenticated ? (
        <div className='admin__grid'>
          {adminConfigs.map((config) => {
            const resourceItems = records[config.key] || []
            const editingItemId = editingRecord[config.key]

            return (
              <article key={config.key} className='admin__panel'>
                <h3>{config.label}</h3>

                <form
                  className='admin__form'
                  onSubmit={(event) => {
                    event.preventDefault()
                    handleCreate(config.key)
                  }}
                >
                  {config.fields.map((field) => (
                    <Field
                      key={field.name}
                      field={field}
                      value={forms[config.key][field.name]}
                      onChange={(event) => handleFieldChange(config.key, field.name, event.target.value)}
                    />
                  ))}

                  <button
                    type='submit'
                    className='btn btn--outline admin__submit'
                    disabled={submittingKey === config.key}
                  >
                    {submittingKey === config.key ? 'Enregistrement...' : `Ajouter ${config.label.toLowerCase()}`}
                  </button>
                </form>

                {loadingRecords ? <p className='admin__loading'>Chargement...</p> : null}

                <div className='admin__records'>
                  {resourceItems.map((item) => {
                    const isEditing = editingItemId === item.id

                    return isEditing ? (
                      <RecordEditor
                        key={`${config.key}-${item.id}`}
                        config={config}
                        item={item}
                        onCancel={() => handleEditCancel(config.key)}
                        onSave={(payload) => handleEditSave(config.key, item.id, payload)}
                      />
                    ) : (
                      <article key={`${config.key}-${item.id}`} className='admin__record'>
                        <div className='admin__record-header'>
                          <RecordSummary config={config} item={item} />
                          <div className='admin__record-actions'>
                            <button
                              type='button'
                              className='btn btn--plain'
                              onClick={() => handleEditStart(config.key, item.id)}
                            >
                              Modifier
                            </button>
                            <button
                              type='button'
                              className='btn btn--plain'
                              onClick={() => handleDelete(config.key, item.id)}
                            >
                              Supprimer
                            </button>
                          </div>
                        </div>

                        <RecordDetails config={config} item={item} />
                      </article>
                    )
                  })}
                </div>
              </article>
            )
          })}
        </div>
      ) : null}
    </section>
  )
}

export default Admin
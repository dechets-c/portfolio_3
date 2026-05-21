import './Skills.css'

const SkillGroup = ({ title, items }) => {
  if (!items.length) return null

  return (
    <div className='skills__group'>
      <h3 className='skills__group-title'>{title}</h3>
      <ul className='skills__list'>
        {items.map((skill) => (
          <li key={`${title}-${skill}`} className='skills__list-item btn btn--plain'>
            {skill}
          </li>
        ))}
      </ul>
    </div>
  )
}

const Skills = ({ skills }) => {
  const hasSkills = Object.values(skills).some((group) => group.length > 0)

  if (!hasSkills) return null

  return (
    <section className='section skills' id='skills'>
      <h2 className='section__title'>Skills</h2>
      <SkillGroup title='Competences' items={skills.competences} />
      <SkillGroup title='Languages' items={skills.langages} />
      <SkillGroup title='Tools' items={skills.outils} />
    </section>
  )
}

export default Skills

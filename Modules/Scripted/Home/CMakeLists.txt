#-----------------------------------------------------------------------------
set(MODULE_NAME Home)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
  )

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  Resources/Icons/Gears.png
  Resources/UI/${MODULE_NAME}.ui
  Resources/UI/Settings.ui
  Resources/Home.qss
  Resources/openlifu-database/empty_db/systems/.keep
  Resources/openlifu-database/empty_db/subjects/subjects.json
  Resources/openlifu-database/empty_db/users/users.json
  Resources/openlifu-database/empty_db/protocols/protocols.json
  Resources/openlifu-database/empty_db/transducers/transducers.json
  )

slicerFunctionAddPythonQtResources(MODULE_PYTHON_QRC_RESOURCES
  Resources/${MODULE_NAME}.qrc
  )

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS} ${MODULE_PYTHON_QRC_RESOURCES}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
  )


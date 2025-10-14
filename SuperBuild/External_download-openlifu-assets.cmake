set(proj download-openlifu-assets)

# Set dependency list
set(${proj}_DEPENDENCIES python-sliceropenlifu-requirements)

# Include dependent projects if any
ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)

ExternalProject_Add(${proj}
  ${${proj}_EP_ARGS}
  DOWNLOAD_COMMAND ""
  SOURCE_DIR ${CMAKE_BINARY_DIR}/${proj}
  BUILD_IN_SOURCE 1
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ${PYTHON_EXECUTABLE} -c "import openlifu; openlifu.util.assets.download_and_install_modnet(); openlifu.util.assets.download_and_install_kwave_assets();"
  LOG_INSTALL 1
  DEPENDS
    ${${proj}_DEPENDENCIES}
  )

ExternalProject_GenerateProjectDescription_Step(${proj} VERSION ${_version})

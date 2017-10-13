{
  'targets': [
    {
      "target_name": "<(module_name)",
      "type": "loadable_module",
      "product_prefix": "",
      "product_extension": "node",
      "sources": [
          "src/MurmurHash3.cpp", 
          "src/node_murmurhash3.cc"
      ],
      "cflags": ["-fexceptions"],
      "cflags_cc": ["-fexceptions"],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exception"],
      "include_dirs" : [
          "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ["OS == 'win'", {
            "msvs_settings": {
              "VCCLCompilerTool": {
                "AdditionalOptions": [ "/EHsc" ]
              }
            }
          }
        ],
        ["OS == 'mac'", {
            "xcode_settings": {
              "GCC_ENABLE_CPP_RTTI": "YES",
               "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
               "MACOSX_DEPLOYMENT_TARGET":"10.8",
               "CLANG_CXX_LIBRARY": "libc++",
               "CLANG_CXX_LANGUAGE_STANDARD":"c++11",
               "GCC_VERSION": "com.apple.compilers.llvm.clang.1_0"
            }
          }
        ]
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
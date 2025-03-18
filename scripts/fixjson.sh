while read pkg ; do
  printf "      {\"name\": \"${pkg}\", "
  desc=$( yay -Si ${pkg} | rg Description | sed -e "s/: /:/" | cut -f2 -d ":")
  printf "\"description\": \"${desc}\"},\n"
 done


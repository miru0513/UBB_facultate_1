#include "ui.h"
#include "service.h"
#include "repository.h"

int main() {
    Repository repo;
    Service service(repo);
    UI ui(service);

    service.addSchool(School("Avram_Iancu", 46.77, 23.60, "15.04.2022"));
    service.addSchool(School("George_Cosbuc", 46.77, 23.58, "18.04.2022"));
    service.addSchool(School("Alexandru_Vaida", 46.75, 23.55, "20.04.2022"));
    service.addSchool(School("Romulus_Guga", 46.76, 23.57, "25.04.2022"));
    service.addSchool(School("Colegiul_Transilvania", 46.78, 23.61, "30.04.2022"));

    ui.run();
    return 0;
}

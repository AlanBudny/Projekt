using System;
using System.Collections.Generic;
using System.Linq;
using System.Media;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace projektrpg
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] player = { 100, 5, 0, 3, 0, 0};
            while (player[0]>0)
            {
                Sklep(player);
            }
            Console.ReadKey();
        }

        public static void Walka(int[] player)
        {
            var enemy_hp = new Random().Next(5 + player[4], 25 + (2 * player[4]));
            var enemy_dmg = new Random().Next(1 + player[4], 6 + (2 * player[4]));
            var enemy_money = new Random().Next(2 + player[4], 10+ (2 * player[4]));
            int[] enemy = {enemy_hp, enemy_dmg, enemy_money};
            
            Console.WriteLine("walczysz z potworem");
            Console.WriteLine($"przeciwnik ma {enemy[0]} zdrowia i {enemy[1]} obrażeń");
            Console.WriteLine($"Masz {player[0]} zdrowia i {player[1]} obrażeń");
            while (enemy[0] > 0)
                {
                    player[0] -= enemy[1] - player[5];
                    Console.WriteLine($"przeciwnik zadaje {enemy[1] - player[5]} obrażeń");
                    Console.WriteLine($"pozostaje ci {player[0]} zdrowia");
                    if (player[0] <= 0)
                    {
                        Console.WriteLine("umierasz");
                        break;
                    }
                    if (player[3] > 0)
                    {
                        Console.WriteLine($"co robisz 1-atakuj, 2-użyj mikstury, posiadasz {player[3]}");
                        int x = int.Parse(Console.ReadLine());
                        if (x == 1)
                        {
                            enemy[0] -= player[1];
                            Console.WriteLine($"zadajesz {player[1]} obrażeń, przeciwnik ma {enemy[0]} zdrowia");
                        }
                        if (x == 2)
                        {
                            player[0] += 10;
                            if (player[0] > 100)
                            {
                                player[0] = 100;
                            }
                            Console.WriteLine($"uleczyłeś 10 zdrowia, masz {player[0]} zdrowia");
                            player[3] -= 1;
                        }
                    }
                    else
                    {
                        Console.WriteLine("co robisz 1-atakuj");
                        int x = int.Parse(Console.ReadLine());
                        if (x == 1)
                        {
                            enemy[0] -= player[1];
                            Console.WriteLine($"zadajesz {player[1]} obrażeń, przeciwnik ma {enemy[0]} zdrowia");
                        }
                    }
                }
                Console.WriteLine($"zabijasz przeciwnika i zdobywasz {enemy[2]} sztuk złota");
                player[4] += 1;
                player[2] += enemy[2];
        }
        public static void Sklep(int[]player)
        {
            Console.WriteLine("Witaj w Mieście!");
            Console.WriteLine($"Gdzie czcesz pójść, masz {player[2]} sztuk złota");
            Console.WriteLine("1-kowal");
            Console.WriteLine("2-zbrojmistrz");
            Console.WriteLine("3-sklep z miksturami");
            Console.WriteLine("4-arena");
            int wybor = int.Parse(Console.ReadLine());
            if (wybor == 1) 
            {
                Console.WriteLine("Witaj Rycerzu. Jaką broń chcesz kupić?");
                Console.WriteLine("1-Miecz(obrażenia-8,koszt-20)");
                Console.WriteLine("2-Topór(obrażenia-12,koszt-35)");
                Console.WriteLine("3-Młot(obrażenia-15,koszt-50)");
                Console.WriteLine("4-Wróć");
                int wybor_broni = int.Parse(Console.ReadLine());
                if (wybor_broni == 1)
                {
                    if (player[2] >= 20)
                    {
                        Console.WriteLine("Kupiłeś miecz");
                        player[1] = 8;
                        player[2] -= 20;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                if (wybor_broni == 2)
                {
                    if (player[2] >= 35)
                    {
                        Console.WriteLine("Kupiłeś topór");
                        player[1] = 12;
                        player[2] -= 35;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                if (wybor_broni == 3)
                {
                    if (player[2] >= 50)
                    {
                        Console.WriteLine("Kupiłeś młot");
                        player[1] = 15;
                        player[2] -= 50;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                else
                {
                    Sklep(player);
                }
            }
            if (wybor == 2)
            {
                Console.WriteLine("Witaj Rycerzu. Jaką zbroję chcesz kupić?");
                Console.WriteLine("1-skórzana(zmniejszenie obrażeń-2,koszt-20)");
                Console.WriteLine("2-kolczuga(zmniejszenie obrażeń-5,koszt-35)");
                Console.WriteLine("3-płytowa(zmniejszenie obrażeń-8,koszt-50)");
                Console.WriteLine("4-Wróć");
                int wybor_zbroji = int.Parse(Console.ReadLine());
                if (wybor_zbroji == 1)
                {
                    if (player[2] >= 20)
                    {
                        Console.WriteLine("Kupiłeś zbroję skórzaną");
                        player[5] = 2;
                        player[2] -= 20;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                if (wybor_zbroji == 2)
                {
                    if (player[2] >= 35)
                    {
                        Console.WriteLine("Kupiłeś kolczugę");
                        player[5] = 5;
                        player[2] -= 35;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                if (wybor_zbroji == 3)
                {
                    if (player[2] >= 50)
                    {
                        Console.WriteLine("Kupiłeś zbroję płytową");
                        player[5] = 8;
                        player[2] -= 50;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
                else
                {
                    Sklep(player);
                }
            }
            if (wybor == 3)
            {
                Console.WriteLine("Witaj w sklepie z miksturami");
                Console.WriteLine("Czy chcesz kupić miksturę za 10 sztuk złota");
                Console.WriteLine("1-Tak");
                Console.WriteLine("2-Nie");
                int decyzja = int.Parse(Console.ReadLine());
                if (decyzja == 1)
                {
                    if (player[2] >= 10)
                    {
                        Console.WriteLine("Kupiłeś miksturę");
                        player[3] += 1;
                        player[2] -= 10;
                        Sklep(player);
                    }
                    else
                    {
                        Console.WriteLine("Nie stać cię biedaku");
                        Sklep(player);
                    }
                }
            }
            if (wybor == 4)
            {
                Walka(player);
            }
        }
    }
}

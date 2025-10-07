<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 01:33:30 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xOTswNDo0NDowNSBQTTsyNzI1"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xOTswNDo0NTowMyBQTTs1O1VzZXI7TEFQVE9QLUE3M0ExQ05UOzIwMjUtMDctMTk7MDQ6MDI6MTYgUE07bGFiXzIuZnByZzs2NjAw"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0yMDswMTozMzozMCBBTTsyMjsyODU0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity" type="Integer" array="False" size=""/>
            <declare name="CoffeePrice, TeaPrice, totalprice" type="Real" array="False" size=""/>
            <assign variable="CoffeePrice" expression="25"/>
            <assign variable="TeaPrice" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu==1">
                <then>
                    <if expression="quantity &lt;= 10">
                        <then>
                            <assign variable="totalprice" expression="CoffeePrice * quantity"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price: &quot;&amp;totalprice&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
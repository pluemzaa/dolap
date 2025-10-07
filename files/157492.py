<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4_lab4.2_fixed"/>
        <attribute name="authors" value="narat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 08:50:50 PM"/>
        <attribute name="created" value="bmFyYXQ7TEVOT1ZPTkFSQVRISVA7MjU2OC0wNy0yMTswODo0Mjo1OSBQTTsyOTAz"/>
        <attribute name="edited" value="bmFyYXQ7TEVOT1ZPTkFSQVRISVA7MjU2OC0wNy0yMTswODo1MDo1MCBQTTsyOzMwMDI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, per, year, temp, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="per"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i&lt;year+1">
                <assign variable="temp" expression="money * (1+(per/100))"/>
                <assign variable="money" expression="temp"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;:&quot;&amp;Tofixed(money,2)" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>
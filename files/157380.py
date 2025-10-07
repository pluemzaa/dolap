<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4_3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 11:40:41 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtTkJHUzEyR0Q7MjU2OC0wNy0xNzsxMToxMzozMyBQTTsyNzUy"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtTkJHUzEyR0Q7MjU2OC0wNy0xNzsxMTo0MDo0MSBQTTsyOzI4NjA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x, y" type="Integer" array="False" size=""/>
            <declare name="sn, en" type="Integer" array="False" size=""/>
            <declare name="m" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:  &quot;" newline="True"/>
            <input variable="m"/>
            <declare name="d" type="Real" array="False" size=""/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="d"/>
            <assign variable="d" expression="1+(d/100)"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="y"/>
            <assign variable="x" expression="1"/>
            <while expression="x &lt;= y">
                <assign variable="m" expression="m*d"/>
                <output expression="&quot;Year &quot; &amp;x&amp; &quot; : &quot;&amp; m" newline="True"/>
                <assign variable="x" expression="x+1"/>
            </while>
        </body>
    </function>
</flowgorithm>
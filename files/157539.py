<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flowchart.lap3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 09:38:49 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMDswOToyMjoxMSBQTTsyNzcz"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQVNBRkZPNlY7MjAyNS0wNy0yMDswOTozODo0OSBQTTsyOzI5MDA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <assign variable="n" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>
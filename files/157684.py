<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="labf5"/>
        <attribute name="authors" value="Legion"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 11:26:31 AM"/>
        <attribute name="created" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTIxOzExOjA3OjA4IEFNOzI5NTE="/>
        <attribute name="edited" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTIxOzExOjI2OjMxIEFNOzM7MzA1OA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="nn, n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="nn"/>
            <output expression="n" newline="True"/>
            <while expression="n &lt; nn">
                <output expression="(n+1)" newline="True"/>
                <assign variable="n" expression="n+1"/>
            </while>
        </body>
    </function>
</flowgorithm>